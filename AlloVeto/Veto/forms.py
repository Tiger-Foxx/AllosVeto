from django import forms
from Veto.models import Consultation,RendezVous

class ConsultationForm(forms.ModelForm):
    
    class Meta:
        model=Consultation
        fields=['email','whatsapp','nom','nomAnimal','ville','date','sexe','age','espece','race','quartier','Vacc','couleur','Motif']
        


class RendezVousForm(forms.ModelForm):
    
    class Meta:
        model=RendezVous
        fields=['email','nom','whatsapp','ville','date','heure','status','Message','quartier']    
        

