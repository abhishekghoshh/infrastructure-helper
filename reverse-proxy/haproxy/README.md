# HAProxy basics


### Sample blogs and configs
- [test.cfg](https://github.com/hnasr/javascript_playground/blob/master/proxy/test.cfg)
- [Restrict API Access With Client Certificates (mTLS)](https://www.haproxy.com/blog/restrict-api-access-with-client-certificates-mtls)
- [Client Certificate Authentication with HAProxy](https://www.loadbalancer.org/blog/client-certificate-authentication-with-haproxy/)

### Youtube videos
- [HAProxy Basics](https://www.youtube.com/playlist?list=PLfnwKJbklIxwxXKiPv5nAgWwmaUvDjW_t)
- [HAProxy](https://www.youtube.com/playlist?list=PLQnljOFTspQUhgfvpgfxc-uFlWElKIBr-)


### Sample config
[haproxy.cfg](./haproxy.cfg)
```
frontend https-in
    bind *:80
    bind *:443  ssl crt server-cert.crt verify required ca-file intermediate-client-ca.crt ca-verify-file client-root-ca.crt
    http-request redirect scheme https unless { ssl_fc }
    default_backend apiservers
```
