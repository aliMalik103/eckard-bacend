from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from eckard_api.models.investment_income import InvestmentIncome
from django.db import connection


class IncomeListingCost(APIView):
   def get(self, request, accountid, projectid):
    try:
      cursor = connection.cursor()
      cursor.execute('select sum("totalIncome") as "incomeToDate", case when sum("acquiredNma") is null then 0 else sum("acquiredNma") end as "availableNma" from (select i.id as "investmentId", case when ii."totalIncome" is null then 0 else ii."totalIncome" end as "totalIncome", "acquiredNma" from (select id, "acquiredNma" from investment where account_id = '+str(accountid)+' and project_id = '+str(projectid)+' and not "isDeleted" and "acquiredNma" > 0) i left join (select investment_id, sum(income) as "totalIncome" from investment_income where not "isDeleted" group by investment_id  ) ii on ii.investment_id = i.id)t')
      row = cursor.fetchone()
      cursor.execute('select case when sum("nma") is null then 0 else sum("nma") end as "listedNma" from listing l join status s on s.id = l.status_id and s.status = '+"'Active'"+' where not l."isDeleted" and account_id = '+str(accountid)+' and project_id = '+str(projectid)+' ')
      row2 = cursor.fetchone()
      data = {}
      data["incomeToDate"] = row[0]
      data["availableNma"] = row[1] - row2[0]
      data["totalNma"]=row[1]
      return Response(data)
    except InvestmentIncome.DoesNotExist:
      return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)  