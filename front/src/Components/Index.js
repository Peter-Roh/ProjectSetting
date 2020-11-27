import React from 'react';
import { Link } from 'react-router-dom';


class Index extends React.Component {
    render() {
        return (
                <>
                    <div>Hello World!</div>
                    <Link to="/test"><div>next</div></Link>
                </>
        );
    }
}

export default Index;
