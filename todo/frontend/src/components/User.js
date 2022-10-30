import React from 'react';
import './Styles.css';
import {Link} from "react-router-dom";

const UserItem = ({user}) => {
    return (
        <tr>
            <td>
                <Link to={`/users/${user.id}`}>
                    {user.firstname}
                </Link>
            </td>
            <td>{user.lastname}</td>
            <td>{user.email}</td>
        </tr>
    )
}


const UserList = (
    {
        users
    }
) => {
    return (
        <table>
            <th>First name</th>
            <th>Last name</th>
            <th>Email</th>
            {users.map((user_) => <UserItem user={user_}/>)}
        </table>
    )
}

export default UserList
