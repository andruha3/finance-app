from . import ma


class CompanySchema(ma.Schema):
    class Meta:
        fields = ("Name", "Date", "Open", "High", "Low", "Close", "Adj_Close", "Volume")
