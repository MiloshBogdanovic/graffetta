from __future__ import print_function
from mailmerge import MailMerge
from datetime import date



def create_bonus_facciate(condo_name, condo_fiscal_code, condo_street, condo_city, condo_province, rep_name, rep_fiscal_code, rep_street, rep_number, rep_city, rep_province, owner_title, subject_of_intervention, total_price, vat_price, date_of_condo_meeting, name_of_bank_for_payment, duration_of_works, date_of_payment_from_condo_to_aurica, pec, street_address, email):
    template = "bonus-facciata.docx"
    document = MailMerge(template)
    print(document.get_merge_fields())
    document.merge(
        condo_name=condo_name,
        condo_fiscal_code=condo_fiscal_code,
        condo_street=condo_street,
        condo_city=condo_city,
        condo_province=condo_province,
        rep_name=rep_name,
        rep_fiscal_code=rep_fiscal_code,
        rep_street=rep_street,
        rep_number=rep_number,
        rep_city=rep_city,
        rep_province=rep_province,
        owner_tile=owner_title,
        subject_of_intervention=subject_of_intervention,
        total_price=total_price,
        vat_price=vat_price,
        date_of_condo_meeting=date_of_condo_meeting,
        name_of_bank_for_payment=name_of_bank_for_payment,
        duration_of_works=duration_of_works,
        date_of_payment_from_condo_to_aurica=date_of_payment_from_condo_to_aurica,
        pec=pec,
        street_address=street_address,
        email=email
        )
        ##TODO: Check to see where the calculation values go inside the contract
    document.write('bonus-facciata-translated.docx')
