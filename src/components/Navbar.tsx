import { ReactNode } from "react";
import { Link, useMatch, useResolvedPath } from "react-router-dom";

type CustomLinkProps = {
  to: string;
  children: ReactNode;
  [key: string]: any;
};

export default function Navbar() {
  return (
    <nav className="nav">
      <Link to="/" className="site-title">
        NJGMC
      </Link>
      <ul>
        <CustomLink to="/library">LIBRARY</CustomLink>
        <CustomLink to="/events">EVENTS</CustomLink>
        <CustomLink to="/members">MEMBERS</CustomLink>
      </ul>
    </nav>
  );
}

function CustomLink({ to, children, ...props }: Readonly<CustomLinkProps>) {
  const resolvedPath = useResolvedPath(to);
  const isActive = useMatch({ path: resolvedPath.pathname, end: true });

  return (
    <li className={isActive ? "active" : ""}>
      <Link to={to} {...props}>
        {children}
      </Link>
    </li>
  );
}
