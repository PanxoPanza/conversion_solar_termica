# Fuentes verificadas para `11_ManejoSolarTermico_Edificio.ipynb`

Revision realizada el 2026-06-08.

## PDFs descargados o confirmados en esta carpeta

- `86554.pdf`: Kim, CaraDonna y Parker (2024), NREL/TP-5500-86554, *End-Use Savings Shapes Measure Documentation: Window Film*. Descargado desde el espejo institucional `https://www.nlr.gov/docs/fy24osti/86554.pdf` porque `nrel.gov` no resolvia desde la consola local. DOI: https://doi.org/10.2172/2447836
- `80171.pdf`: DOE/NREL (2022), *Pathway to Zero Energy Windows: Advancing Technologies and Market Adoption*.
- `bto-electrochromic-window-report-121123.pdf`: DOE (2022/2023), *Better Windows, Better Outcomes: How Electrochromics Improve Health, Productivity, and Efficiency*.
- `EC-Windows-FactSheet_v9.pdf`: LBNL, *Electrochromic Windows Fact Sheet*.

## Correcciones principales aplicadas

- IEA edificios: se corrigio la cifra de emisiones. La pagina actual de IEA Buildings reporta cerca de 26% de emisiones globales relacionadas con energia para la operacion de edificios; el 28% citado antes correspondia a una formulacion antigua/no respaldada por la pagina IEA Energy Efficiency 2025.
- IEA cooling: se retiro la frase "se triplico entre 1990 y 2018". La fuente IEA *The Future of Cooling* respalda que la demanda de enfriamiento podria mas que triplicarse hacia 2050 y que aire acondicionado/ventiladores usan cerca de 20% de la electricidad de edificios.
- Filmes de ventana: se reemplazaron rangos demasiado especificos por la clasificacion y resultados respaldados por NREL 86554. El reporte documenta reducciones de SHGC de 17-71% y mejoras de U-factor de 0-22% segun vidrio base y film.
- Electrochromic windows: se reemplazaron porcentajes universales de ahorro por resultados mas fieles al DOE EC report: casos con ahorros combinados HVAC+iluminacion de 39-48%, reduccion de iluminacion de 36% en un caso, reducciones modeladas de 10-20% en energia HVAC+iluminacion de zona perimetral y 20-30% en demanda peak.
- Costos y vidas utiles: se retiraron costos instalados y vidas utiles exactas cuando no estaban respaldados directamente por las fuentes DOE/NREL/LBNL. Se dejaron como criterios cualitativos de seleccion y durabilidad.
- Cool roofs: se reemplazo "10-20%" por el rango EPA 11-27% de reduccion de demanda peak de enfriamiento, y se agrego el dato DOE de techos reflectivos mas de 50 F (28 C) mas frios que techos convencionales.
- PDRC: se corrigio la cita del DOI 10.1126/science.aat9513. Ese DOI corresponde a Mandal et al. (2018), *Hierarchically porous polymer coatings for highly efficient passive daytime radiative cooling*, no a Zhai et al.
- Chile: las tablas climaticas quedaron marcadas como ordenes de magnitud para discusion, con fuentes reales sugeridas (Unidad 7/Explorador Solar y Direccion Meteorologica de Chile), y se agrego matiz para la costa de Antofagasta por camanchaca/humedad.

