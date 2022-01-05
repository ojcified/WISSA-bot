# WISSA-bot
Ein Discord bot um eine Liste aus Inputs als csv zu erstellen.

Nachdem der Bot erstellt ist und zum Server hinzugefügt wurde(siehe Dokumentation von Discord), muss in der <b>bot.py</b> der Channelname noch ergänzt werden und in der <b>bot.env</b> der TOKEN des Bots hinzugefügt werden (siehe Discord Dokumentation).
Danach ist mit dem Syntax '!wissa Vorname Nachname "Thema"' in dem entsprechenden Channel ein Eintrag in der liste.csv inkl. Timestamp hinzugefügt.

Die file.c übernimmt 3 strings als argumente, fügt diese zusammen und fügt am Ende einen Timestamp hinzu.
