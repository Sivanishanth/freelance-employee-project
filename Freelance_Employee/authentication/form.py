from django import forms


class Client_Register(forms.Form):
    Name = forms.CharField(label="User Name", max_length=30)
    Mail = forms.CharField(label="Mail", max_length=30)
    Phoneno = forms.CharField(label="Contact", max_length=30)
    Password = forms.CharField(label="Password", max_length=30)
class Freelance_Register(forms.Form):
   Name = forms.CharField(label="User Name", max_length=30)
   Role = forms.CharField(label="Role", max_length=30)
   Expertise = forms.CharField(label="Expertise", max_length=30)
   Age = forms.CharField(label="Age", max_length=2)
   EmpId = forms.CharField(label="Employee Id")
   Mail = forms.CharField(label="E-Mail", max_length=30)
   Phno = forms.CharField(label="Phone Number", max_length=30)
   
Softwares= [
    ('windows', 'Windows'),
    ('mac', 'Mac'),
    ('linux', 'Linux'),
    ('ubuntu', 'Ubuntu'),
]
class Teac_Team(forms.Form):
    Name=forms.CharField(label="Name")
    Mail=forms.CharField(label="Email")
    Id=forms.CharField(label="ID")
    Choice=forms.ChoiceField(choices=Softwares)
    Location=forms.CharField(label="Location")
    Salary=forms.CharField(label="Salary")
    Job_type=forms.CharField(label="Job Type")
    Age=forms.CharField(label="Age")
    Gender=forms.CharField(label="Gender")
    experience=forms.CharField(label="Experience")