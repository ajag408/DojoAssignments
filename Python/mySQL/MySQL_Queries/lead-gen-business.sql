-- SELECT SUM(billing.amount)
-- FROM billing
-- WHERE MONTH(billing.charged_datetime) = 3 AND YEAR(billing.charged_datetime) = 2012;

-- SELECT SUM(billing.amount)
-- FROM billing
-- WHERE billing.client_id = 2;

-- SELECT COUNT(sites.site_id)
-- FROM sites
-- WHERE sites.client_id = 10;

-- SELECT COUNT(sites.site_id)/(12*(SELECT MAX(YEAR(sites.created_datetime)) - 
--   MIN(YEAR(sites.created_datetime)) FROM sites))
-- FROM sites
-- WHERE sites.client_id = 1


-- SELECT COUNT(sites.site_id)/(12*(SELECT MAX(YEAR(sites.created_datetime)) - 
--   MIN(YEAR(sites.created_datetime)) FROM sites))
-- FROM sites
-- WHERE sites.client_id = 20;

-- SELECT COUNT(leads.leads_id)
-- FROM leads
-- WHERE (YEAR(leads.registered_datetime) = 2011 AND 
--   MONTH(leads.registered_datetime) = 2 AND 
--   DAYOFMONTH(leads.registered_datetime) <= 15) OR 
--   (YEAR(leads.registered_datetime) = 2011 AND
--   MONTH(leads.registered_datetime) = 1)

-- SELECT clients.first_name, clients.last_name, clients.client_id, COUNT(leads.leads_id)
-- FROM clients
-- LEFT JOIN sites
-- ON sites.client_id = clients.client_id
-- LEFT JOIN leads
-- ON sites.site_id = leads.site_id
-- WHERE YEAR(leads.registered_datetime) = 2011
-- GROUP BY clients.client_id;

-- SELECT clients.first_name, clients.last_name, COUNT(leads.leads_id), MONTH(leads.registered_datetime)
-- FROM clients
-- LEFT JOIN sites 
-- ON sites.client_id = clients.client_id
-- LEFT JOIN leads
-- ON sites.site_id = leads.site_id
-- WHERE YEAR(leads.registered_datetime) = 2011 AND 
-- 	(MONTH(leads.registered_datetime)>=1 AND
--     MONTH(leads.registered_datetime)<=6)
-- GROUP BY leads.leads_id;
-- 
-- SELECT clients.first_name, clients.last_name, sites.domain_name, COUNT(leads.leads_id)
-- FROM leads
-- LEFT JOIN sites
-- ON leads.site_id = sites.site_id
-- LEFT JOIN clients
-- ON sites.client_id = clients.client_id
-- WHERE YEAR(leads.registered_datetime) = 2011
-- GROUP BY leads.site_id
-- ORDER BY clients.client_id;
-- 

-- SELECT clients.first_name, clients.last_name, sites.domain_name, COUNT(leads.leads_id)
-- FROM leads
-- LEFT JOIN sites
-- ON leads.site_id = sites.site_id
-- LEFT JOIN clients
-- ON sites.client_id = clients.client_id
-- GROUP BY leads.site_id

-- SELECT clients.client_id, SUM(billing.amount), MONTH(billing.charged_datetime), 
-- 	YEAR(billing.charged_datetime)
-- FROM clients
-- LEFT JOIN billing
-- ON billing.client_id = clients.client_id
-- GROUP BY MONTH(billing.charged_datetime), YEAR(billing.charged_datetime), clients.client_id
-- ORDER BY clients.client_id

SELECT clients.first_name, clients.last_name, GROUP_CONCAT(sites.domain_name)
FROM clients
JOIN sites
ON sites.client_id = clients.client_id
GROUP BY clients.client_id
