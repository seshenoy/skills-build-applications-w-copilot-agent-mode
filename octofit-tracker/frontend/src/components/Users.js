import React, { useEffect, useState } from 'react';

function Users() {
    const [users, setUsers] = useState([]);

    useEffect(() => {
        fetch('https://effective-space-goggles-9q77wqjpr4gf9xq4-8000.app.github.dev/api/users/')
            .then(response => response.json())
            .then(data => setUsers(data));
    }, []);

    return (
        <div className="card">
            <div className="card-body">
                <h1 className="card-title">Users</h1>
                <table className="table table-striped">
                    <thead>
                        <tr>
                            <th>ID</th>
                            <th>Username</th>
                        </tr>
                    </thead>
                    <tbody>
                        {users.map(user => (
                            <tr key={user.id}>
                                <td>{user.id}</td>
                                <td>{user.username}</td>
                            </tr>
                        ))}
                    </tbody>
                </table>
            </div>
        </div>
    );
}

export default Users;
