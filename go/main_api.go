package main

import (
    "github.com/ant0ine/go-json-rest/rest"
    "log"
    "net/http"
    "fmt"
    "os/exec"
    "strings"
)

type Data struct {
    Name    string `json:"name"`
    DoorStatus    string `json:"doorStatus"`
}

func main() {
    api := rest.NewApi()
    api.Use(rest.DefaultDevStack...)

    router, err := rest.MakeRouter(
        rest.Get("/api/getDoorStatus", func(w rest.ResponseWriter, req *rest.Request) {
            name := "ADENTIS RaspberryPi 3 Model B located somewhere"

            cmd := exec.Command("/root/go/code/door.py")
            out, err := cmd.CombinedOutput()
            if err != nil { fmt.Println(err); }

            doorStatus := string(out)
            doorStatus = strings.Replace(doorStatus, "\n", "", -1)

            data := Data{Name: name, DoorStatus: doorStatus}

            w.WriteJson(&data)
        }),
    )

    if err != nil {
        log.Fatal(err)
    }

    api.SetApp(router)

    log.Println("API listening on port 80 under /getDoorStatus .")
    log.Fatal(http.ListenAndServe(":80", api.MakeHandler()))
}
