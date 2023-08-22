const fs = require('fs');

class Repository {
    retrieve() {}
    persist(users) {}
}

class UsersFileRepository extends Repository {
    constructor(file) {
        super();
        this.file = file;
    }
    retrieve() {
        if (fs.existsSync(this.file)) {
            let data = fs.readFileSync(this.file, 'utf-8');
            if (data) {
                return JSON.parse(data)
            }
        }
        return []
    }
    persist(users) {
        if (fs.existsSync(this.file)) {
            let data = JSON.stringify(users);
            fs.writeFileSync(this.file, data);
        }
    }
}

class UsersMemoryRepository extends Repository {
    constructor() {
        super();
        this.users = [];
    }
    retrieve() {
        return this.users;
    }
    persist(users) {
        this.users = users;
    }
}

module.exports = {
    UsersFileRepository, UsersMemoryRepository
}