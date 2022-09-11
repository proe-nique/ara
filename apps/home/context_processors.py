def engine(request):
    context = {
        'site_name_short':'ARA',
        'site_name_long':'Augmented Reality and Automation',
        'site_name_full':'Augmented Reality and Automation (Pvt) Ltd',
        'moto':'Vehicle Tracking Solutions',
        'site_about':'We are a leading Zimbabwe provider for vehicle tracker solutions that remotely control, track and monitor your vehicle using wireless technology with innovative data platform service.',
        'site_bio':"Augmented Reality and Automation (Pvt) Ltd is a privately held, wholly Zimbabwe owned company, registered under company number 12021/2022. We offer our services all over Zimbabwe. The nature of our busness is to fix, supply, monitor, service vehicle trackers and the provision of related services. The wireless sensor monitoring technology intergrates the vehicle owners with the reality of their vehicles in the real world. ARA is committed to helping companies implement transperant monitoring and intelligent control of many links in the transportation proccess, creating an efficient system while satisfying company's management tracking service and information needs",
    }
    return context