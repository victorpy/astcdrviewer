from models import TrunksAccountcodes,Accounts,Payments,Rate,RateGroup,Cdr,RatedCdr
from table import Table
from table.columns import Column

class TrunksAccountcodesTable(Table):
    accountcode = Column(field='accountcode', header='accode') 
    description = Column(field='description', header='desc')
    class Meta:
	model = TrunksAccountcodes

class CdrTable(Table):
    calldate = Column(field='calldate', header='Fecha')
    clid = Column(field='clid', header='CallerID')
    dst = Column(field='dst', header='Destino')
    billsec = Column(field='billsec', header='Duracion')
    
    class Meta:
        model = Cdr


class PaymentsTable(Table):
    date = Column(field='date', header='Fecha')
    #accountcode = Column(field='accountcode', header='Acode')
    amount = Column(field='amount', header='Monto')
    comments = Column(field='comments', header='Descripcion')
    class Meta:
        model = Payments

class RateTable(Table):
    destination = Column(field='destination', header='Destino')
    description = Column(field='description', header='Descripcion')
    amount1 = Column(field='amount1', header='Costo Inicial')
    cadence1 = Column(field='cadence1', header='Cadencia1(seg.)')
    amount2 = Column(field='amount2', header='Costo Siguientes')
    cadence2 = Column(field='cadence2', header='Cadencia2(seg.)')

    class Meta:
        model = Rate


class RatedCdrTable(Table):
    calldate =  Column(field='calldate', header='Fecha') 
    clid = Column(field='clid', header='Caller ID')
    dst =  Column(field='dst', header='Destino')
    amount = Column(field='amount', header='Monto')
    #accountcode = 
    billsec = Column(field='billsec', header='Tiempo')
    class Meta:
        model = RatedCdr
