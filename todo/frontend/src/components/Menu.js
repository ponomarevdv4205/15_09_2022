import React from "react";
import './Styles.css'

function Menu() {
    return (
        <div class="top">
            <div class="container top__box">
                <div class="top__info">
                    <h1 class="zag__level__1">Web-сервис для работы с ToDo-заметками</h1>
                        <p class="text">
                            Проект на базе Django REST framework
                        </p>
                        <ul class="menu-bar">
                            <li>Users</li>
                            <li>Project</li>
                            <li>ToDo</li>
                        </ul>
                </div>
            </div>
        </div>
    );
}

export default Menu;
///
