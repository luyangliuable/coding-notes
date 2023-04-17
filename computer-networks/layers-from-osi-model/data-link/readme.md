# Datalink Layer

<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [Datalink Layer](#datalink-layer)
    - [Datalink Mac Sublayer](#datalink-mac-sublayer)

<!-- markdown-toc end -->


## Datalink Mac Sublayer

```


                                                            Application Data                        <- Application Layer
                                          TCP Header                                                <- TCP Layer
                            IP header                                                               <- IP Layer
              LLC Header                                                                            <- LLC Layer
  Mac Header                                                                    MAC Trailer         <- MAC Layer
 ---------------------------------------------------------------------------------------------------
|           |           |              |               |                     |                      |
 ---------------------------------------------------------------------------------------------------
                                       <-----------TCP Segment -------------->
                        <---------------------IP Datagram ------------------->
             <--------------------LLC Protocol Data Unit -------------------->
             <--------------------MAC frame----------------------------------->
```
