# Projekta apraksts
Šis projekts ir uzdevumu plānotājs (task planner), kas palīdz lietotājiem organizēt savus darbus pēc prioritātēm. Lietotājs ievada uzdevumu ar tā nosaukumu, beigu termiņu, aptuveno izpildes laiku un prioaritāte tiek aprēķināta, pēc tā programma uzdevumus ievieto heap datu struktūrā pēc aprēķinātās prioaritātes, kas ļauj pēc tam izveidot heap ar svarīgākajiem uzdevumiem augšā un, kad lietotājs izvēlās opciju, parādīt nākamo uzdevumu, programma no heap izvelk ar mazāko prioaritātes koeficientu uzdevumu jeb svarīgako uz doto brīdi un izvada to konsole priekš lietotāja.

#################################################################################################################################

Programma lietotājam ļauj:

Pievienot jaunus uzdevumus ar:

Uzdevuma nosaukumu

Termiņu (beigu datumu)

Paredzamo izpildes laiku stundās

Automātiski aprēķināt katra uzdevuma prioritāti, pamatojoties uz:

Atlikušo laiku līdz termiņam (dienās)

Nepieciešamo izpildes laiku (stundās)

Parādīt pilno uzdevumu sarakstu prioritāšu secībā

Iegūt nākamo visaugstākās prioritātes uzdevumu

#################################################################################################################################

Izmantotās Python bibliotēkas

heapq - Šī ir iebūvēta Python bibliotēka, kas ļauj strādāt ar kaudzes (heap) datu struktūru. Tika izmantota, jo:

Ļauj efektīvi uzturēt uzdevumus prioritāšu secībā izmantojot min-heap struktūru

Ļauj ātri iegūt augstākās prioritātes uzdevumu

Ir daudz efektīvāka nekā rēķināšana ar sarakstiem

datetime - Iebūvēta bibliotēka datumu un laika apstrādei. Izmantota, lai:

Apstrādātu lietotāja ievadītos termiņus

Aprēķinātu atlikušo laiku līdz termiņam

Veiktu prioritāšu aprēķinus

#################################################################################################################################

Projekta datu struktūras:

Projektā tika izmantotas šādas datu struktūras:

Task klase - Reprezentē vienu uzdevumu ar šādiem atribūtiem:

name - uzdevuma nosaukums

deadline - termiņš (datums)

duration_hours - paredzamais izpildes laiks stundās

priority - aprēķinātā prioritāte

TaskPlanner klase - Galvenā projekta datu struktūra, kas:

Uztur uzdevumu kopu kā kaudzi (heap) pēc prioaritātes, šīs programmas gadījumā kā min-kaudzi (min-heap), lai pēc prioaritātes koeficienta aprēķināšanas, mazākās vērtības jeb svarīgākie uzdevumi būtu heap augšdaļā

Nodrošina metodes darbam ar uzdevumiem

Realizē prioritāšu kārtošanas loģiku

Programmatūras izmantošanas metodes
Instalācija
Projekts neprasa papildu instalāciju, izņemot Python 3.x

Visas nepieciešamās bibliotēkas jau ir iekļautas Python standarta bibliotēkā

Lietošanas instrukcija
Palaidiet programmu ar komandu: python planning.py

Izvēlnē izvēlieties vajadzīgo darbību:

1. Pievienot jaunu uzdevumu (Add a new task) - ievadiet uzdevuma detaļas

2. Iegūt nākamo uzdevumu (Get next task to complete) - iegūst augstākās prioritātes uzdevumu

3. Apskatīt visus uzdevumus (View all tasks) - parāda visus uzdevumus prioritāšu secībā

4. Iziet (Exit) - pārtrauc programmas darbību

Darbības princips

Katram uzdevumam tiek aprēķināta prioritāte:

prioritāte = (dienas līdz termiņam) / (izpildes laiks stundās)

Jo mazāks prioritātes koeficients, jo augstāka uzdevuma prioritāte

Uzdevumi tiek sakārtoti kaudzē (heap) pēc prioritātēm

Augstākās prioritātes uzdevumi tiek izpildīti pirmie

Ievades formāts

Termiņš: Jābūt ievadītam formātā YYYY-MM-DD (piemēram, 2023-12-31)

Izpildes laiks: Jānorāda stundās (var būt decimāldaļa, piemēram 1.5)

Šis projekts ir izstrādāts, lai atvieglotu sava laika plānošanu un izpildāmo uzdevumu secības plānošanu

#################################################################################################################################

Lai programmu padarītu labāku (uzlabotu) var implementēt datubāzi, kas saglabās uzdevumus un to atribūtus, lai katru reizi nav jāievada uzdevumi no jauna, tad ir vēl iespēja pievienot GUI, piemēram, izmantojot python GUI bibliotēku Tkinter un arī var implementēt webscraping, lai piekļūtu ortus e-studijām un izgūtu uzdevumus, to termiņus, lai vēl vairāk automizētu darbību.