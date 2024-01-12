import { Outlet } from "react-router-dom"
import "./HomeLayout.style.css"




function HomeLayout (props: any) {
    return <div className="HomeLayout">
        <div  className="PageContent" >
        <Outlet />
        </div>
    </div>
}

export default HomeLayout