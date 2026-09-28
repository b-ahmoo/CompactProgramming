#Task 5. Create a dictionary with the events in Dortmund and the date of the event. List all events that were running during the Night of Museums in Dortmund on 19th September 2026. 

dortmund_events = {
    "Dortmund Christmas Market (Weihnachtsmarkt)": "30.11.2026",
    "Mayday Electronic Music Festival": "30.04.2026",
    "Juicy Beats Festival": "19.09.2026",
    "ExtraSchicht (Night of Industrial Culture)": "19.09.2026",
    "FestiRamadan": "14.03.2026",
    "Lichterfest Westfalenpark": "30.08.2026",
    "Micro! Festival": "05.09.2026"
}

for event, date in dortmund_events.items():
    if (date == "19.09.2026"):
        print(event + " : " + date)