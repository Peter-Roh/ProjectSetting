import React from 'react';
import axios from 'axios';


class Test extends React.Component {
    constructor(props) {
        super(props);

        this.handlePost = this.handlePost.bind(this);

        this.state = {
            data: null
        };
    }

    componentDidMount() {
        axios.get("http://localhost:8000/api/test/")
        .then((res) => {
            this.setState({
                data: res.data,
            });
        });
    }

    handlePost() {
        axios.post("http://localhost:8000/api/test/", {
            name: 'posted!'
        })
        .then((res) => {
            console.log(res);
            this.setState({
                data: this.state.data.concat(res.data),
            });
        });

    }

    render() {
        return (
            <>
                <div>
                {
                    this.state.data !== null ?
                    this.state.data.map((elt) => {
                        return (
                            <>
                                <div>{elt.name}</div>
                            </>
                        );
                    })
                    :
                    null
                }
                </div>
                <button onClick={this.handlePost}>Post</button>
            </>
        );
    }
}

export default Test;
