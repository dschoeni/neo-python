

from neo.Core.TX.Transaction import Transaction,TransactionType
import sys

class MinerTransaction(Transaction):

    Nonce = None

    NetworkFee = 0

    def __init__(self, *args, **kwargs):
        super(MinerTransaction, self).__init__(*args, **kwargs)
        self.Type = TransactionType.MinerTransaction

    def Size(self):
        return self.Size() + sys.getsizeof(int)

    def DeserializeExclusiveData(self, reader):
        self.Nonce = reader.ReadUInt32()

    def SerializeExclusiveData(self, writer):
        writer.WriteUInt32(self.Nonce)


    def OnDeserialized(self):
        raise NotImplementedError()
