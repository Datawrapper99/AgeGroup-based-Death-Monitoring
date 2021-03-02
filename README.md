# AgeGroup-based-Death-Monitoring

### Can we predict German deaths?? Let's find out.
Hi all fellow hobby-epidemiologists,

this analysis delves into German deaths based on data by [destatis](https://www.destatis.de/DE/Themen/Gesellschaft-Umwelt/Bevoelkerung/Sterbefaelle-Lebenserwartung/Tabellen/sonderauswertung-sterbefaelle.html;jsessionid=D5059F400B46230E5778173BD23E8094.internet712) . Let's find out, if we can predict German deaths by treating viruses as black-box model and predict seasonal death-waves only from past observations (death and population distributions). So we don't care about the virus classification schemes like flu A/B or Corona. We also don't care about DNA, the infectiousness or dangerousness of viruses. The only prior information, we may incorporate is that virus-waves emerge during winter and heat-waves occur during summer. The virus-season starts every year in the beginning of October and ends in the end of May (see RKI). The rest of the year will be denoted as heat-season.



### Let's start with plotting annual deaths decomposed into Age Groups
We start by decomposing the total death signal into age groups. Look at the ![plot: stacked_by_agegroups_deaths_destatis](https://github.com/[Datawrapper99]/[AgeGroup-based-Death-Monitoring]/blob/[main]//misc/stacked_by_agegroups_deaths_destatis.JPG?raw=true)
 and try to find your age group. Can you see waves in your age group? No?,.. then you probably belong to a young age group. Yes!, then you belong definitly to an older age group. And this our first observation. Old people cause seasonality in deaths and young people don't. Let's re-check this for each year. However, the pattern remains the same: Below age 45 age-bands remain mainly flat (non-seasonal age groups) while above 45 age-bands start to form waves (seasonal age groups).


