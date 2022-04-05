from django import forms
from .models import *
from django.forms import ModelForm
from django.forms.widgets import FileInput, Select, TextInput
from dal import autocomplete
from .csv_reader import get_cap_list

# class FileFieldForm(forms.Form):
#     file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))


class FileRequiredForm(ModelForm):
    class Meta:
        model = FileRequired
        exclude = ['id']
        labels = {
            'file': 'Scegli file',
            'name': 'Nome del file',
        }
        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control m-1',
                'type': 'text',
            }),
            'file': FileInput(attrs={
                'class': 'form-control-file',
                'type': 'file',
                'name': 'file',

            }),
        }


class StatusFileForm(ModelForm):
    class Meta:
        model = StatusFile
        exclude = ['file']
        labels = {
            'status': 'STATUS',
        }
        widgets = {
            'status': Select(attrs={
                'class': 'custom-select m-1',
            }),
        }


class BonusVillaForm(ModelForm):
    class Meta:
        model = BonusVilla
        exclude = ['id', 'catastal', 'beneficiary', 'professionals', 'interventions', 'overall_interventions', 'driving_interventions', 'trailed_interventions']
        labels = {}
        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
            }),
            'street': TextInput(attrs={
                'class': 'form-control',
            }),
            'cap': TextInput(attrs={
                'class': 'form-control',
            }),
            'municipality': TextInput(attrs={
                'class': 'form-control',
            }),
            'province': TextInput(attrs={
                'class': 'form-control',
            }),
            'email': EmailInput(attrs={
                'class': 'form-control',
            }),
            'pec_mail': EmailInput(attrs={
                'class': 'form-control',
            }),
            'bank_id': Select(attrs={
                'class': 'form-control',
            }),
        }


class BonusCondoForm(ModelForm):
    class Meta:
        model = BonusCondo
        exclude = ['id', 'beneficiary', 'catastal', 'professionals', 'interventions', 'overall_interventions',
                   'common_interventions', 'subjective_interventions', 'admin_legal', 'admin_individual']
        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
            }),
            'street': TextInput(attrs={
                'class': 'form-control',
            }),
            'cap': TextInput(attrs={
                'class': 'form-control',
            }),
            'common_location': TextInput(attrs={
                'class': 'form-control',
            }),
            'fiscal_code': TextInput(attrs={
                'class': 'form-control',
            }),
            'province': TextInput(attrs={
                'class': 'form-control',
            }),
            'email': EmailInput(attrs={
                'class': 'form-control',
            }),
            'pec_mail': EmailInput(attrs={
                'class': 'form-control',
            }),
            'bank_id': Select(attrs={
                'class': 'form-control',
            }),
        }


class InterventionsForm(ModelForm):
    class Meta:
        model = Interventions
        exclude = ['id', 'date_of_assembly']
        labels = {
            'art119_c1_a': 'Intervento “trainante” ai sensi dell’art. 119 c. 1 lett a), D.L. 34/2020: intervento di “isolamento termico” (con materiali isolanti che rispettano i “CAM” del D.M. dell’Ambiente del 11/10/2017) delle superfici opache verticali (pareti isolanti o cappotti, anche sulla superficie intera delle pareti), orizzontali (pavimenti e coperture) e inclinate (falde di copertura del sottotetto), che interessa l’involucro dell’Immobile, con un’incidenza superiore al 25% della superficie disperdente lorda;',
            'art119_c1_b': ' Intervento “trainante” ai sensi dell’art. 119 c. 1 lett. b), D.L. 34/2020 per la “sostituzione degli impianti di climatizzazione invernale” esistenti nell’Immobile con (i) impianti per il riscaldamento, il raffrescamento o la fornitura di acqua calda sanitaria, a condensazione, con efficienza almeno pari alla classe A (regolamento UE n. 811/2013), a pompa di calore, ivi compresi gli impianti ibridi o geotermici ovvero con impianti di microcogenerazione, a collettori solari; (ii) allaccio a sistemi di teleriscaldamento efficiente (art. 2, c. 2, lett. tt), D.Lgs. 102/2014), solo nelle aree non metanizzate nei comuni montani non interessati dalle procedure europee di infrazione n. 2014/2147 o 2015/2043',
            'art119c_4': "Intervento “trainante” ai sensi dell’art. 119 c. 4, D.L. 34/2020 per la realizzazione di misure antisismiche dell'articolo 16, commi da 1-bis a 1-septies, D.L. 63/2013.",
            'art1_c345': 'art. 1, co. 345, L. 296/2006 per la realizzazione di strutture opache verticali (pareti) ed orizzontali (coperture e pavimenti);',
            'art1_c345_art14': 'art. 1, co. 345, L. 296/2006 e art. 14, D.L. 63/2013 per la installazione di finestre comprensive di infissi delimitanti il volume riscaldato verso l’esterno ovvero vani non riscaldati, con i requisiti di trasmittanza termica di legge;',
            'art1_c346': 'art. 1, co. 346, L. 296/2006 per l’installazione di pannelli solari per la produzione di acqua calda;',
            'art1_c286': 'art. 1, co. 286, L. 244/2007 per la sostituzione di impianti di climatizzazione invernale con caldaie dotate di pompe di calore ad alta efficienza o impianti geotermici a bassa entalpia;',
            'art14_2_1': 'art. 14, co. 2.1 D.L. 63/2013 per la sostituzione di impianti di climatizzazione invernale con caldaie a condensazione con efficienza almeno pari alla classe A di cui al Regolamento UE n. 811/2013',
            'art14_2_1_B': 'art. 14, co. 2.1 D.L. 63/2013 per la sostituzione di impianti di climatizzazione invernale con caldaie a condensazione con efficienza almeno pari alla classe A di cui al Regolamento UE n. 811/2013 e contestuale installazione di sistemi di termoregolazione di cui alle classi V, VI o VIII della Comunicazione della Commissione 2014/C 207/02',
            'art14_2_1_C': 'art. 14, co. 2.1 D.L. 63/2013 per la sostituzione di impianti di climatizzazione invernale con apparecchi ibridi, costituiti da pompa di calore integrata con caldaia a condensazione, assemblati in fabbrica per funzionare in abbinamento tra loro;',
            'art4_c4': 'art. 4, co. 4, D.L. 201/2011 per la sostituzione di scaldacqua tradizionali con scaldacqua a pompa di calore per la produzione di acqua calda sanitaria che rispettino i valori fissati dalle relative tabelle vigenti,',
            'art1_c88': 'art. 1, co. 88, L. 208/2015 per l’acquisto ed installazione di dispositivi multimediali per il controllo da remoto degli impianti di riscaldamento o produzione di acqua calda o di climatizzazione delle unità abitative;',
            'art14_c2': 'art. 14, co. 2 lett b) del D.L. 63/2013 per l’acquisto ed installazione di schermature solari di cui all’allegato M), D.Lgs. 311/2006;',
            'art14_c2_bis': 'art. 14, co. 2-bis, D.L. 63/2013 par l’acquisto ed installazione di impianti di climatizzazione invernale con impianti dotati di generatori di calore alimentati da biomasse combustibili;',
            'art14_c2_b_bis': 'art. 14, co. 2, lett. b-bis) D.L. 63/2013 per l’acquisto ed installazione di micro-cogeneratori che permettano un risparmio di energia primaria (PES) di almeno il 20%, come disciplinato dall’allegato III del D.M. 4.8.2011; ',
            'trailed_art16_bis_c': 'Interventi “trainati” per l’eliminazione di barriere architettoniche di cui all’art. 16-bis c. 1 lett. e) del TUIR, anche ove effettuati in favore di persone con più di 65 anni ai sensi dell’art. 119, c. 2, D.L. 34/2020;',
            'trailed_art119_c': 'Interventi “trainati” di installazione di impianti solari fotovoltaici con, contestuale o successiva installazione di, sistemi di accumulo, ai sensi dell’art. 119, c. 5 e c. 6, D.L. 34/2020;',
            'towed_art119_c': 'Interventi “trainati” di installazione di colonnine di ricarica di veicoli elettrici, ai sensi dell’art. 119, c. 8, D.L. 34/2020',
            'description': "DESCRIZIONE SINTETICA DELL'INTERVENTO",
        }
        widgets = {
            'description': Textarea(attrs={
                'class': 'ml-0',
                'id': 'description'
            }),
        }


class InterventionsCondoForm(ModelForm):
    class Meta:
        model = Interventions
        exclude = ['id']
        labels = {
            'art119_c1_a': 'Intervento “trainante” ai sensi dell’art. 119 c. 1 lett a), D.L. 34/2020: intervento di “isolamento termico” (con materiali isolanti che rispettano i “CAM” del D.M. dell’Ambiente del 11/10/2017) delle superfici opache verticali (pareti isolanti o cappotti, anche sulla superficie intera delle pareti), orizzontali (pavimenti e coperture) e inclinate (falde di copertura del sottotetto), che interessa l’involucro dell’Immobile, con un’incidenza superiore al 25% della superficie disperdente lorda;',
            'art119_c1_b': ' Intervento “trainante” ai sensi dell’art. 119 c. 1 lett. b), D.L. 34/2020 per la “sostituzione degli impianti di climatizzazione invernale” esistenti nell’Immobile con (i) impianti per il riscaldamento, il raffrescamento o la fornitura di acqua calda sanitaria, a condensazione, con efficienza almeno pari alla classe A (regolamento UE n. 811/2013), a pompa di calore, ivi compresi gli impianti ibridi o geotermici ovvero con impianti di microcogenerazione, a collettori solari; (ii) allaccio a sistemi di teleriscaldamento efficiente (art. 2, c. 2, lett. tt), D.Lgs. 102/2014), solo nelle aree non metanizzate nei comuni montani non interessati dalle procedure europee di infrazione n. 2014/2147 o 2015/2043',
            'art119c_4': "Intervento “trainante” ai sensi dell’art. 119 c. 4, D.L. 34/2020 per la realizzazione di misure antisismiche dell'articolo 16, commi da 1-bis a 1-septies, D.L. 63/2013.",
            'art1_c345': 'art. 1, co. 345, L. 296/2006 per la realizzazione di strutture opache verticali (pareti) ed orizzontali (coperture e pavimenti);',
            'art1_c345_art14': 'art. 1, co. 345, L. 296/2006 e art. 14, D.L. 63/2013 per la installazione di finestre comprensive di infissi delimitanti il volume riscaldato verso l’esterno ovvero vani non riscaldati, con i requisiti di trasmittanza termica di legge;',
            'art1_c346': 'art. 1, co. 346, L. 296/2006 per l’installazione di pannelli solari per la produzione di acqua calda;',
            'art1_c286': 'art. 1, co. 286, L. 244/2007 per la sostituzione di impianti di climatizzazione invernale con caldaie dotate di pompe di calore ad alta efficienza o impianti geotermici a bassa entalpia;',
            'art14_2_1': 'art. 14, co. 2.1 D.L. 63/2013 per la sostituzione di impianti di climatizzazione invernale con caldaie a condensazione con efficienza almeno pari alla classe A di cui al Regolamento UE n. 811/2013',
            'art14_2_1_B': 'art. 14, co. 2.1 D.L. 63/2013 per la sostituzione di impianti di climatizzazione invernale con caldaie a condensazione con efficienza almeno pari alla classe A di cui al Regolamento UE n. 811/2013 e contestuale installazione di sistemi di termoregolazione di cui alle classi V, VI o VIII della Comunicazione della Commissione 2014/C 207/02',
            'art14_2_1_C': 'art. 14, co. 2.1 D.L. 63/2013 per la sostituzione di impianti di climatizzazione invernale con apparecchi ibridi, costituiti da pompa di calore integrata con caldaia a condensazione, assemblati in fabbrica per funzionare in abbinamento tra loro;',
            'art4_c4': 'art. 4, co. 4, D.L. 201/2011 per la sostituzione di scaldacqua tradizionali con scaldacqua a pompa di calore per la produzione di acqua calda sanitaria che rispettino i valori fissati dalle relative tabelle vigenti,',
            'art1_c88': 'art. 1, co. 88, L. 208/2015 per l’acquisto ed installazione di dispositivi multimediali per il controllo da remoto degli impianti di riscaldamento o produzione di acqua calda o di climatizzazione delle unità abitative;',
            'art14_c2': 'art. 14, co. 2 lett b) del D.L. 63/2013 per l’acquisto ed installazione di schermature solari di cui all’allegato M), D.Lgs. 311/2006;',
            'art14_c2_bis': 'art. 14, co. 2-bis, D.L. 63/2013 par l’acquisto ed installazione di impianti di climatizzazione invernale con impianti dotati di generatori di calore alimentati da biomasse combustibili;',
            'art14_c2_b_bis': 'art. 14, co. 2, lett. b-bis) D.L. 63/2013 per l’acquisto ed installazione di micro-cogeneratori che permettano un risparmio di energia primaria (PES) di almeno il 20%, come disciplinato dall’allegato III del D.M. 4.8.2011; ',
            'trailed_art16_bis_c': 'Interventi “trainati” per l’eliminazione di barriere architettoniche di cui all’art. 16-bis c. 1 lett. e) del TUIR, anche ove effettuati in favore di persone con più di 65 anni ai sensi dell’art. 119, c. 2, D.L. 34/2020;',
            'trailed_art119_c': 'Interventi “trainati” di installazione di impianti solari fotovoltaici con, contestuale o successiva installazione di, sistemi di accumulo, ai sensi dell’art. 119, c. 5 e c. 6, D.L. 34/2020;',
            'towed_art119_c': 'Interventi “trainati” di installazione di colonnine di ricarica di veicoli elettrici, ai sensi dell’art. 119, c. 8, D.L. 34/2020',
            'description': "DESCRIZIONE SINTETICA DELL'INTERVENTO",
        }
        widgets = {
            'description': Textarea(attrs={
                'class': 'ml-0',
                'id': 'description'
            }),
            'date_of_assembly': DateInput(attrs={
                'class': 'form-control',
                'id': 'date_of_assembly',
                'type': 'date'
            })
        }


class CatastalDataForm(ModelForm):
    class Meta:
        model = CatastalData
        exclude = ['id']


class OverallInterCostsNOVatForm(ModelForm):
    class Meta:
        model = OverallInterCostsNOVat
        exclude = ['id']


class InterDrivingWorkNOVatForm(ModelForm):
    class Meta:
        model = InterDrivingWorkNOVat
        exclude = ['id']


class InterTrailedWorkNOVatForm(ModelForm):
    class Meta:
        model = InterTrailedWorkNOVat
        exclude = ['id']


class CommonWorkNOVatForm(ModelForm):
    class Meta:
        model = CommonWorkNOVat
        exclude = ['id']


class SubjectiveWorkNOVatForm(ModelForm):
    class Meta:
        model = SubjectiveWorkNOVat
        exclude = ['id']


class AdministrationIndividualForm(ModelForm):
    class Meta:
        model = AdministrationIndividual
        exclude = ['id']
        widgets = {
            'dob': DateInput(attrs={
                'class': 'form-control',
                'id': 'dob',
                'type': 'date'
            })
        }


class AdministrationLegalForm(ModelForm):
    class Meta:
        model = AdministrationLegal
        exclude = ['id']



# class ModelFormWithFileField(ModelForm):
#     class Meta:
#         model = BonusVillaFiles
#         exclude = ['id']
#         labels = {}
#         widgets = {
#             'files': FileInput(attrs={
#                 'class': 'form-control-file',
#                 'type': 'file'
#             }),
#             'images': FileInput(attrs={
#                 'class': 'form-control-file',
#                 'type': 'file'
#             })}