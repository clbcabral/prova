const service = require('../service');

describe('Users crud test', () => {
    test('listing users empty', () => {
        const users = service.listUsers();
        expect(users.length).toBe(0);
    });
    test('insert one user', () => {
        const user = {
            'id': 1,
            'nome': 'fulano'
        };
        const newUser = service.insertUser(user);
        const users = service.listUsers();
        expect(user.id).toBe(newUser.id);
        expect(user.nome).toBe(newUser.nome);
        expect(users.length).toBe(1);
    });
});