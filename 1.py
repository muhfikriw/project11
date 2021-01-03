def diffDate(x):
    import datetime
    now = datetime.datetime.now()
    from datetime import datetime
    masuk = datetime.strptime(x, "%Y-%m-%d")
    rumus = masuk - now
    print(abs(rumus.days))

diffDate("2019-12-24")