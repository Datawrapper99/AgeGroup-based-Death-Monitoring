# AgeGroup-based-Death-Monitoring

### Can we predict German deaths?? Let's find out.
Hi all fellow hobby-epidemiologists,

this analysis delves into German deaths based on data by [destatis](https://www.destatis.de/DE/Themen/Gesellschaft-Umwelt/Bevoelkerung/Sterbefaelle-Lebenserwartung/Tabellen/sonderauswertung-sterbefaelle.html;jsessionid=D5059F400B46230E5778173BD23E8094.internet712) . Let's find out, if we can predict German deaths by treating viruses as black-box model and predict seasonal death-waves only from past observations (death and population distributions). So we don't care about the virus classification schemes like flu A/B or Corona. We also don't care about DNA, the infectiousness or dangerousness of viruses. The only prior information, we may incorporate is that virus-waves emerge during winter and heat-waves occur during summer. The virus-season starts every year in the beginning of October and ends in the end of May (see RKI). The rest of the year will be denoted as heat-season.



### Let's start with plotting annual deaths decomposed into Age Groups
We start by decomposing into age groups. 



