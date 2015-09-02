[33mCREATE TABLE[0m [1m"domains_domaintmp"[0m (
    [32;1m"name"[0m [32mvarchar(128)[0m [33mNOT NULL[0m [33mPRIMARY KEY[0m,
    [32;1m"zone_id"[0m [32mvarchar(128)[0m [33mNOT NULL[0m,
    [32;1m"registrer_date"[0m [32mdate[0m [33mNOT NULL[0m,
    [32;1m"release_date"[0m [32mdate[0m [33mNOT NULL[0m,
    [32;1m"registrator"[0m [32mvarchar(128)[0m [33mNOT NULL[0m
)
;BULK INSERT domains_domaintmp FROM /home/alex/git/ALL-RU.txt WITH (FIELDTERMINATOR = ' ', ROWTERMINATOR = '\n') UPDATE domains_domain SET zone = domains_domaintmp.zone, registrer_date = domains_domaintmp.registrer_date, release_date = domains_domaintmp.release_date, registrator = domains_domaintmp.registrator FROM domains_domaintmp WHERE  domains_domain.name = domains_domaintmp.name;DROP TABLE domains_domaintmp;