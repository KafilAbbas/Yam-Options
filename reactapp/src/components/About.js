import {useState, useEffect,useRef} from "react";
import Navbar from './navbar'
import './component.css'
function AboutMe(){
    return(
        <div>
            <div>
            <Navbar/>
            </div>
        <div className="HomeBox">
        <div className="Home">
            <p className="para">
                <h2> Developed by Kafil Abbas Momin</h2>
                </p>
                <p className="para2">
                <h2>Currently studying at IIITB</h2>
            </p>
        </div>
        </div>
        </div>
    );
}
export default AboutMe