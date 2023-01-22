import React from 'react';
import './Styles.css';
import {Link} from 'react-router-dom';

const TodoItem = ({ todo, delete_todo }) => {
    return (
        <tr>
            <td>{todo.user}</td>
            <td>{todo.user}</td>
            <td>{todo.modified}</td>
            <td>{todo.text}</td>
            <button onClick={()=>delete_todo(todo.id)} type='button'>Удалить</button>
        </tr>
    )
}

const TodoList = ({ todos, delete_todo }) => {
    return (
        <div>
        <table>
            <th>Project ID</th>
            <th>User ID</th>
            <th>Modified</th>
            <th>Text</th>
            <th>Действие</th>
            {todos.map((todo_, index)=> <TodoItem key={index} todo={todo_} delete_todo={delete_todo}/> )}
        </table>
        <br></br>
        <Link to='/todos/create'>Создать Заметку</Link>
        </div>
    )
}

export default TodoList
