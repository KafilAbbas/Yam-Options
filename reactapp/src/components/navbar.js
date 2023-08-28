import { useRef } from "react";
import { FaBars, FaTimes } from "react-icons/fa";
import "./navbar_css.css";
import logo from './logo-png.png'
function Navbar() {
	const navRef = useRef();

	const showNavbar = () => {
		navRef.current.classList.toggle(
			"responsive_nav"
		);
	};

	return (
		<header>
            <div >
			<a  href="/"><img className='logo' src={logo} alt="Yam Option" /></a>
            </div>
			<nav ref={navRef}>
				<a href="/">Home</a>
				<a href="/option_chain">Option Chain</a>
				<a href="/stradle" >Stradle</a>
				<button
					className="nav-btn nav-close-btn"
					onClick={showNavbar}>
					<FaTimes />
				</button>
			</nav>
			<button
				className="nav-btn"
				onClick={showNavbar}>
				<FaBars />
			</button>
		</header>
	);
}

export default Navbar;