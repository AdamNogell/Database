# Methods
 - LINADMIX - ADMIXTURE output analysed (https://pmc.ncbi.nlm.nih.gov/articles/PMC10212583/)
 - ADMIXTOOLS
 - sequenceTOOLS (https://github.com/stschiff/sequenceTools) from  https://www.nature.com/articles/ncomms10408#Sec8
 - rarecoal - from the same article (https://github.com/stschiff/rarecoal)

# Temp
  3: country - NOT
  4: continent - NOT
  5: geo_group - DONE
  6: culture - TBC
  7: epoch - TBC
  8: group - TBC
  9: comment - DONE
  13: site - NOT(?)

# geo_group
> new geo_groups:
  Caribbean, Oceania, east Asia, central Asia, Latin America, central Africa, south Africa
> countries with no geo_group:
  Canada
  India
  Russia
  USA
> Questions:
  1) How to distinguish between paleolithic periods?
  2) Why is there no Middle Ages or Classical Ages?
  3) How to know if I should use location or country in 'group'

csvcut -c 12 AADR_data/metadata_for_sequences_not_present_in_AmtDB_geneticID.csv | head

Group ID
Albania_EarlyModern_oCaucasus
Bahamas_SouthAndros_Ceramic
Belize_4600BP
Bulgaria_EIA
Czech_IA_Hallstatt
Dominican_ElSoco_Ceramic
England_BellBeaker_highEEF
England_MIA_LIA_o1_lc
England_N_Megalithic

csvcut -c 13 AADR_data/metadata_for_sequences_not_present_in_AmtDB_geneticID.csv | head

Locality
"Barç (Southeast, Korça Basin)"
"South Andros, Sanctuary Blue Hole"
Mayahak Cab Pek
Kapitan Andreevo (South)
"NW Bohemia, Louny, Stradonice"
El Soco
"England, Wiltshire, Amesbury Down"
"England, Hampshire, Winnall Down"
"England, Gloucestershire, Cheltenham, Hazleton North"

>Continue line 243 - copy epoch extract and make a new one but with Early/Late etc. 