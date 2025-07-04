import torch.nn as nn
import torch.nn.functional as F
import torch
import pytorch_lightning as pl


class MNISTModule(pl.LightningModule):
    def __init__(self, hparams):
        super().__init__()
        self.save_hyperparameters(hparams)
        layers = self.hparams.layers if 'layers' in self.hparams else [100]
        layer = lambda h: nn.Sequential(nn.Linear(layers[h], layers[h+1]), nn.ReLU())
        self.mlp = nn.Sequential(
            nn.Linear(28 * 28, layers[0]),
            nn.ReLU(),
            *[layer(h) for h in range(len(layers)-1)],
            nn.Linear(layers[-1], 1)
        )
        
    def forward(self, x):
        x = x.float() / 255
        return self.mlp(x.view(x.size(0), -1)).squeeze(-1)

    def predict(self, x):
        self.eval()
        with torch.no_grad():
            return torch.sigmoid(self(x))

    def training_step(self, batch, batch_idx):
        x, y = batch
        y_hat = self(x)
        loss = F.binary_cross_entropy_with_logits(y_hat, y.float())
        preds = torch.sigmoid(y_hat) > 0.5
        acc = (preds.long() == y).float().mean()
        self.log('loss', loss)
        self.log('acc', acc, prog_bar=True)
        return loss

    def validation_step(self, batch, batch_idx):
        x, y = batch
        y_hat = self(x)
        loss = F.binary_cross_entropy_with_logits(y_hat, y.float())
        preds = torch.sigmoid(y_hat) > 0.5
        acc = (preds.long() == y).float().mean()
        self.log('val_loss', loss, prog_bar=True)
        self.log('val_acc', acc, prog_bar=True)

    def configure_optimizers(self):
        return torch.optim.Adam(self.parameters())
