import time 
from datetime import datetime

class Date(object):
    
    months = {
            1: {
                'name': 'janvier',
                'days': 31
            },
            2: {
                'name': 'février',
                'days': 28
            },
            3: {
                'name': 'mars',
                'days': 31
            },
            4: {
                'name': 'avril',
                'days': 30
            },
            5: {
                'name': 'mai',
                'days': 31
            },
            6: {
                'name': 'juin',
                'days': 30
            },
            7: {
                'name': 'juillet',
                'days': 31
            },
            8: {
                'name': 'août',
                'days': 31
            },
            9: {
                'name': 'septembre',
                'days': 30
            },
            10: {
                'name': 'octobre',
                'days': 31
            },
            11: {
                'name': 'novembre',
                'days': 30
            },
            12: {
                'name': 'décembre',
                'days': 31
            }
        }
    
    days = {
        1: {
            'fr': 'lundi',
            'eng': 'Monday'
        },
        2: {
            'fr': 'mardi',
            'eng': 'Tuesday'
        },
        3: {
            'fr': 'mercredi',
            'eng': 'Wednesday'
        },
        4: {
            'fr': 'jeudi',
            'eng': 'Thursday'
        },
        5: {
            'fr': 'vendredi',
            'eng': 'Friday'
        },
        6: {
            'fr': 'samedi',
            'eng': 'Saturday'
        },
        7: {
            'fr': 'dimanche',
            'eng': 'Sunday'
        }
    }
    
    def __init__(self) -> None:
        """Initialise la classe Date
        """
        # Vérifie si l'année est bissextile et modifie le dictionnaire du nombre de jours de février
        self.months[2]['days'] = 29 if self.isBesextile(datetime.today().year) else 28
    
    def isBesextile(self, year: int) -> bool:
        """Vérifie si une année est bissextile

        Args:
            year (int): L'année à vérifier

        Returns:
            bool: True si l'année est bissextile, False sinon
        """
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    
    def intToMonth(self, month: int) -> str:
        """Convertit un chiffre en mois

        Args:
            month (int): Le chiffre du mois

        Returns:
            str: Le mois en lettres
        """
        return self.months[month]['name']
    
    def engDayToFr(self, jour: str) -> str:
        """Convertit un jour en anglais en français

        Args:
            jour (str): Le jour en anglais
            decalage (int, optional): Le décalage à appliquer. Defaults to 0.

        Returns:
            str: Le jour en français
        """
        for day in self.days:
            if self.days[day]['eng'].lower() == jour.lower():
                return self.days[day.key()]['fr'][:3]
    
    def getDate(self, shift: int) -> str:
        """Renvoie la date du jour
        
        Args:
            shift (int): Le décalage à appliquer

        Returns:
            str: La date du jour
        """
        # Récupère la date du jour
        day = datetime.today()
        
        # Applique le décalage
        for _ in range(shift):
            day = day + datetime.timedelta(days=1)
        
        # Renvoie les informations du jour concerné
        return {
            "jour": self.engDayToFr(day.strftime('%A')),
            "chiffre": day.day,
            "mois": day.month,
        }
        
    def getDatesList(self, numberOfDay: int = 7):
        dateList = {}
        for dayShift in range(7):
            dateList[f'jour{dayShift}'] = self.getDate(dayShift)
            
        return dateList