package main

import (
	"fmt"
	"net/http"
	"net/http/httputil"
	"net/url"

	"github.com/gin-gonic/gin"
)

func proxy(c *gin.Context) {
	remote, err := url.Parse("http://127.0.0.1:8000")
	if err != nil {
		panic(err)
	}
	proxy := httputil.ReverseProxy{
		Director: func(req *http.Request) {
			req.URL.Scheme = remote.Scheme
			req.URL.Host = remote.Host
			req.URL.Path = c.Param("proxy")
			fmt.Printf("%+v | %+v\n", req.URL, req.Header)
		},
	}
	proxy.ServeHTTP(c.Writer, c.Request)
}

func main() {
	r := gin.Default()
	r.Any("/*proxy", proxy)
	r.Run(":8080")
}
