TEMPERATURA = [
    [# TENA
        [# SEMANA 1
            {"DIA": "LUNES", "TEMPERATURA": 35},
            {"DIA": "MARTES", "TEMPERATURA": 26},
            {"DIA": "MIERCOLES", "TEMPERATURA": 16},
            {"DIA": "JUEVES", "TEMPERATURA": 12},
            {"DIA": "VIERNES", "TEMPERATURA": 32},
            {"DIA": "SABADO", "TEMPERATURA": 21},
            {"DIA": "DOMINGO", "TEMPERATURA": 24}
        ],
        [# SEMANA 2
            {"DIA": "LUNES", "TEMPERATURA": 20},
            {"DIA": "MARTES", "TEMPERATURA": 34},
            {"DIA": "MIERCOLES", "TEMPERATURA": 34},
            {"DIA": "JUEVES", "TEMPERATURA": 27},
            {"DIA": "VIERNES", "TEMPERATURA": 34},
            {"DIA": "SABADO", "TEMPERATURA": 19},
            {"DIA": "DOMINGO", "TEMPERATURA": 13}
        ],
        [# SEMANA 3
            {"DIA": "LUNES", "TEMPERATURA": 30},
            {"DIA": "MARTES", "TEMPERATURA": 28},
            {"DIA": "MIERCOLES", "TEMPERATURA": 36},
            {"DIA": "JUEVES", "TEMPERATURA": 22},
            {"DIA": "VIERNES", "TEMPERATURA": 32},
            {"DIA": "SABADO", "TEMPERATURA": 31},
            {"DIA": "DOMINGO", "TEMPERATURA": 34}
        ],
        [# SEMANA 4
            {"DIA": "LUNES", "TEMPERATURA": 30},
            {"DIA": "MARTES", "TEMPERATURA": 34},
            {"DIA": "MIERCOLES", "TEMPERATURA": 34},
            {"DIA": "JUEVES", "TEMPERATURA": 37},
            {"DIA": "VIERNES", "TEMPERATURA": 34},
            {"DIA": "SABADO", "TEMPERATURA": 39},
            {"DIA": "DOMINGO", "TEMPERATURA": 33}
        ],
    ],
    [# ARCHIDONA
        [# SEMANA 1
            {"DIA": "LUNES", "TEMPERATURA": 30},
            {"DIA": "MARTES", "TEMPERATURA": 28},
            {"DIA": "MIERCOLES", "TEMPERATURA": 36},
            {"DIA": "JUEVES", "TEMPERATURA": 22},
            {"DIA": "VIERNES", "TEMPERATURA": 32},
            {"DIA": "SABADO", "TEMPERATURA": 31},
            {"DIA": "DOMINGO", "TEMPERATURA": 34}
        ],
        [# SEMANA 2
            {"DIA": "LUNES", "TEMPERATURA": 30},
            {"DIA": "MARTES", "TEMPERATURA": 34},
            {"DIA": "MIERCOLES", "TEMPERATURA": 34},
            {"DIA": "JUEVES", "TEMPERATURA": 37},
            {"DIA": "VIERNES", "TEMPERATURA": 34},
            {"DIA": "SABADO", "TEMPERATURA": 39},
            {"DIA": "DOMINGO", "TEMPERATURA": 33}
        ],
        [# SEMANA 3
            {"DIA": "LUNES", "TEMPERATURA": 30},
            {"DIA": "MARTES", "TEMPERATURA": 28},
            {"DIA": "MIERCOLES", "TEMPERATURA": 36},
            {"DIA": "JUEVES", "TEMPERATURA": 22},
            {"DIA": "VIERNES", "TEMPERATURA": 32},
            {"DIA": "SABADO", "TEMPERATURA": 31},
            {"DIA": "DOMINGO", "TEMPERATURA": 34}
        ],
        [# SEMANA 4
            {"DIA": "LUNES", "TEMPERATURA": 30},
            {"DIA": "MARTES", "TEMPERATURA": 34},
            {"DIA": "MIERCOLES", "TEMPERATURA": 34},
            {"DIA": "JUEVES", "TEMPERATURA": 37},
            {"DIA": "VIERNES", "TEMPERATURA": 34},
            {"DIA": "SABADO", "TEMPERATURA": 39},
            {"DIA": "DOMINGO", "TEMPERATURA": 33}
        ],
    ],
    [# PUYO
        [# SEMANA 1
            {"DIA": "LUNES", "TEMPERATURA": 30},
            {"DIA": "MARTES", "TEMPERATURA": 28},
            {"DIA": "MIERCOLES", "TEMPERATURA": 36},
            {"DIA": "JUEVES", "TEMPERATURA": 22},
            {"DIA": "VIERNES", "TEMPERATURA": 32},
            {"DIA": "SABADO", "TEMPERATURA": 31},
            {"DIA": "DOMINGO", "TEMPERATURA": 34}
        ],
        [# SEMANA 2
            {"DIA": "LUNES", "TEMPERATURA": 30},
            {"DIA": "MARTES", "TEMPERATURA": 34},
            {"DIA": "MIERCOLES", "TEMPERATURA": 34},
            {"DIA": "JUEVES", "TEMPERATURA": 37},
            {"DIA": "VIERNES", "TEMPERATURA": 34},
            {"DIA": "SABADO", "TEMPERATURA": 39},
            {"DIA": "DOMINGO", "TEMPERATURA": 33}
        ],
        [# SEMANA 3
            {"DIA": "LUNES", "TEMPERATURA": 30},
            {"DIA": "MARTES", "TEMPERATURA": 28},
            {"DIA": "MIERCOLES", "TEMPERATURA": 36},
            {"DIA": "JUEVES", "TEMPERATURA": 22},
            {"DIA": "VIERNES", "TEMPERATURA": 32},
            {"DIA": "SABADO", "TEMPERATURA": 31},
            {"DIA": "DOMINGO", "TEMPERATURA": 34}
        ],
        [# SEMANA 4
            {"DIA": "LUNES", "TEMPERATURA": 30},
            {"DIA": "MARTES", "TEMPERATURA": 34},
            {"DIA": "MIERCOLES", "TEMPERATURA": 34},
            {"DIA": "JUEVES", "TEMPERATURA": 37},
            {"DIA": "VIERNES", "TEMPERATURA": 34},
            {"DIA": "SABADO", "TEMPERATURA": 39},
            {"DIA": "DOMINGO", "TEMPERATURA": 33}
        ],
    ],
]
suma_temperatura = float()
peomedio_semanal = float()
c = int()
x = int()
for ciudad in TEMPERATURA:
    x += 1
    if x == 1:
        print("=========================================================")
        print("PROMEDIO SEMANAL DE TEMPERATURAS DE LA CIUDAD DE TENA")
        print("=========================================================")
    if x == 2:
        print("=========================================================")
        print("PROMEDIO SEMANAL DE TEMPERATURAS DE LA CIUDAD ARCHIDONA")
        print("=========================================================")
    if x == 3:
        print("=========================================================")
        print("PROMEDIO SEMANAL DE TEMPERATURAS DE LA CIUDAD PUYO")
        print("=========================================================")
    for semana  in ciudad:
        c +=1
        for dia in semana:
            suma_temperatura += dia["TEMPERATURA"]
        promedio_semanal = suma_temperatura / 7
        print(f"La semana {c}, tuvo un promedio de temperatura {promedio_semanal}")
        print()
        suma_temperatura = 0
    c=0