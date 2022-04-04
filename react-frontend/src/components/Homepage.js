import { useState } from 'react';
import '../assets/css/Homepage.css'
import homevideo from '../assets/media/intro.mp4';
import homelogo from '../assets/media/lbwhite.png';

const Homepage = ()=> {
    const [ IsAuthenticated, setIsAuthenticated ] = useState('false');

    return (
        <div className="container">
            <div className="content">
                <section>                        
                    <div className="links">
                        <a href="https://ra.co/dj/lerb/" target="_blank" rel="noopener noreferrer">TOUR DATES</a>
                        <a href="https://medium.com/@leroybuliro" target="_blank" rel="noopener noreferrer">BLOG</a>
                        <a href="https://podcasts.apple.com/us/podcast/kubonga-show/id1470474649">PODCAST</a>
                        <a href="/account/auth">INSIDERS</a>
                    </div>                        
                    <div className="imagediv">
                        <img className="image" src={ homelogo } alt="leroy" />
                    </div>                        
                    {/* <div className="intro">
                        <span>Logged in as @</span>
                    </div>                                             */}
                </section>
                <video src={ homevideo } autoplay muted loop></video>
            </div>
        </div>
    )
}

export default Homepage