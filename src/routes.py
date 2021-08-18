from flask_restful import Resource
from . import api, db
from .schemas import CompanySchema
from .models import *


class Finance(Resource):
    companySchema = CompanySchema()

    def get(self, company_name=None):
        if not company_name:
            companies = (
                db.session.query(Companies).order_by(Companies.Date.desc()).all()
            )
            return self.companySchema.dump(companies, many=True), 200
        company = (
            db.session.query(Companies)
            .filter_by(Name=company_name)
            .order_by(Companies.Date.desc())
            .all()
        )
        if not company:
            return "", 404
        return self.companySchema.dump(company, many=True), 200


api.add_resource(Finance, "/", "/<company_name>", strict_slashes=False)
