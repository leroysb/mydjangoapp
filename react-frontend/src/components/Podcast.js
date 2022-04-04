import '../assets/css/podcast.css'
import podcastImage from '../assets/media/ksp.jpg';
import iconTT from '../assets/media/ksp.jpg';
import iconIG from '../assets/media/ksp.jpg';

const Podcast = ()=> {
    return (
        <main>
            <nav class="topnav">
                <a id="navlogo" href="/home">
                    <img class="logoimg" src="{% static 'core/media/lbwhite.png' %}" alt="logo" />
                </a>
                <div class="navmenu">
                    <a href="{% url 'core:event' %}">EVENTS</a>
                    <a href="{% url 'core:blogpage' %}">BLOG</a>
                </div>
                <div class="menuBtn">
                    <div class="menu-btn__burger"></div>
                </div>
            </nav>
        
            <div className="podpage">
                <section className="intro">
                    <img src={ podcastImage } alt="Kubonga Show" style={{ width: '100%', height: 'auto' }} />
                    <div className="side">
                        <h2 style={{ color: '#ffffff' }}>About</h2>
                        <p className="pod-deet">Translated to "talk" in Swahili slang - "Kubonga" is a seasonal, meandering conversation with guests where they tell their stories, converse on topics close to their heart and, yeah, just have a nice chat.</p>
                    </div>
                    <div className="curve">
                        <svg data-name="Layer 1" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 120" preserveAspectRatio="none">
                            <path d="M985.66,92.83C906.67,72,823.78,31,743.84,14.19c-82.26-17.34-168.06-16.33-250.45.39-57.84,11.73-114,31.07-172,41.86A600.21,600.21,0,0,1,0,27.35V120H1200V95.8C1132.19,118.92,1055.71,111.31,985.66,92.83Z" class="shape-fill"></path>
                        </svg>
                    </div>
                </section>
            </div>

            <div class="bottom">
                <div id="footersocial">
                    <a href="https://twitter.com/leroybuliro/" target="_blank" rel="noopener noreferrer"><img src={ iconTT } alt="twitter" width="auto" height="22" /></a>
                    <a href="https://instagram.com/leroybuliro/" target="_blank" rel="noopener noreferrer"><img src={ iconIG } alt="instagram" width="auto" height="22" /></a>
                </div>
                <span>© 2022 Leroy Buliro. All rights reserved.</span>
                <span>
                    <a href="{% url 'core:legal' %}">Legal</a>
                </span>
            </div>
        </main>
    )
}

export default Podcast