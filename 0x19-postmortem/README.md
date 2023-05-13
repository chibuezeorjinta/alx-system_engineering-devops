# **Incident Report:** Expired Certbot Certificate  

  <img src="./pQ9YzVY.gif" width="100%">

  ### **ISSUE SUMMARY:** 😪  
  On June 1, 2023, the SSL certificate for our website expired, resulting in an outage that lasted for two hours from 2:00 PM to 4:00 PM Eastern Standard Time. During this time, users attempting to access our website were greeted with a security warning and were unable to connect securely to our site. Approximately 80% of users attempting to access the site during this time were affected.
  
  ### **ROOT CAUSE:**
  <img src="./face.jpg" width="75%" height="75%">       
  
  
  The root cause of the outage was due to the expiration of our SSL certificate. The certificate was not renewed prior to its expiration, resulting in users being unable to access our site over a secure connection.

  ### **TIMELINE:** 🧐 
  <img src="./ah-shit-here-we-go-again.gif"  width="100%" height="30%">
  
- 2:00 PM EST - The issue was first detected when several users complained about being unable to connect to our site over HTTPS.
- 2:10 PM EST - The incident was escalated to our operations team, who began investigating the issue.
- 2:20 PM EST - The team identified that the SSL certificate had expired, resulting in the outage.
- 2:30 PM EST - The team attempted to renew the certificate, but were unable to do so due to an issue with the certificate authority.
- 3:00 PM EST - The team contacted the certificate authority and were informed that the certificate could be renewed manually, but would take several hours to complete.
- 3:30 PM EST - The team opted to purchase a new SSL certificate from a different certificate authority and installed it on our servers.
- 4:00 PM EST - The new SSL certificate was installed and tested, restoring secure access to our site.
  
### **CORRECTIVE AND PREVENTIVE MEASURES:**  
To prevent similar issues from occurring in the future, we will be implementing the following measures:
  
  - Implement a system to automatically monitor SSL certificate expiration dates and send alerts when certificates are nearing expiration.
  - Establish a process for renewing certificates at least one month prior to their expiration dates.
  - Establish a process for renewing certificates at least one month prior to their expiration dates.
  - Perform a comprehensive review of our incident response process and implement any necessary improvements to ensure timely and effective resolution of future incidents.

### **ACTIONS TAKEN:**  (☞ﾟヮﾟ)☞
  During the incident, the operations team investigated the SSL certificate and attempted to renew it, but were unable to do so due to an issue with the certificate authority. They quickly identified an alternate solution of purchasing a new SSL certificate from a different certificate authority and installed it on our servers. The team then tested the new certificate and confirmed that it was functioning properly, resolving the issue.

### **MISLEADING INVESTIGATION/DEBUGGING PATHS:**  
During the investigation, the team initially assumed that the issue was related to a server configuration error or a network issue. They spent approximately 20 minutes investigating these possibilities before discovering that the issue was actually related to the SSL certificate expiration.
  
  ### **ESCALATION:**  
  The incident was initially escalated to the operations team, who were able to resolve the issue. If the team had been unable to resolve the issue, it would have been escalated to our senior engineering team for further investigation.