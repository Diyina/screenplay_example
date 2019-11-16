from screenpy import Target


url = "https://www.ebay.com"
LOG_IN_LINK = Target.the('log in link').located_by('#gh-ug > a:nth-child(1)')

