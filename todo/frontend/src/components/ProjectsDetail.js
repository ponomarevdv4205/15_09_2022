import React from 'react';
import {useParams} from 'react-router-dom';


const ProjectItem = ({project}) => {

    return (
        <tr>
            <td>
                {project.name}
            </td>
            <td>
                {project.url}
            </td>
            <td>
                {project.users}
            </td>
        </tr>
    )
}

const ProjectsDetail = ({projects}) => {
    let {projectId}= useParams()
    let filter_projects = projects.filter((project)=> project.id==projectId)
    console.log(filter_projects)

    return (
        <table>
            <th>
                Name
             </th>
             <th>
                Url
             </th>
             <th>
                Users
             </th>
             {filter_projects.map((project)=> <ProjectItem project={project}/> )}
        </table>
    )
}

export default ProjectsDetail