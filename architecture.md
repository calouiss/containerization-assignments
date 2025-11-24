flowchart TD

    Client -->|HTTP :80| Nginx

    Nginx -->|/api/books| BooksAPI
    Nginx -->|/api/readers| ReadersAPI
    Nginx -->|/api/staff| StaffAPI

    BooksAPI --- Backend
    ReadersAPI --- Backend
    StaffAPI --- Backend

    subgraph Backend["Backend Network (app_backend)"]
        DB[(Database - future integration)]
    end
