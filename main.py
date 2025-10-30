import datetime 
dat_cloak = {
    
}
def ip_catcher(ip_addr):
    dat_cloak[ip_addr] = {
        "blocked" : 0,
        "attempts" : 0,
        "ports" : [],
        "last_attempt" : ""
     }
def connect_event(ip_addr, port):
        if ip_addr in dat_cloak:
            dat_cloak[ip_addr]["ports"].append(port)
            dat_cloak[ip_addr]["attempts"]+=1
            dat_cloak[ip_addr]["last_attempt"]=datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            if dat_cloak[ip_addr]["attempts"] >= 7 or len(dat_cloak[ip_addr]["ports"]) >= 5:
                dat_cloak[ip_addr]["blocked"] = 1
            logger(ip_addr, port)
        else: 
            ip_catcher(ip_addr)
            dat_cloak[ip_addr]["ports"].append(port)
            dat_cloak[ip_addr]["attempts"]+=1
            dat_cloak[ip_addr]["last_attempt"]=datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            logger(ip_addr, port)
def logger(ip_addr, port):
     time = dat_cloak[ip_addr]["last_attempt"]
     #atn = access to network 
     if dat_cloak[ip_addr]["blocked"] == 0:
          atn = "ALLOWED"
     else:
          atn = "BLOCKED (SUSPICIOUS)"
     log = open("logger.txt", "a")
     log.write(f"time:[{time}] | IP: {ip_addr} | ports: {port} | Status: {atn}\n")
     log.close()

ip = "10.10.267.942"
ip1 = "11.87.167.201"
null = ""
connect_event(ip, 80)
connect_event(ip, 443)
connect_event(ip1, 8080)
print(dat_cloak)