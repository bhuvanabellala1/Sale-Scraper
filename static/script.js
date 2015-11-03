var CommentBox = React.createClass({

        loadDeals: function() {
            $.ajax({
                url: this.props.url,
                dataType: 'json',
                cache: false,
                success: function(deals) {
                    this.setState({deals: deals});
                    console.log(data);
                 }.bind(this),
                error: function(xhr, status, err) {
                    console.error(this.props.url, status, err.toString());
                }.bind(this)
            });
        },
        getInitialState: function() {
            return {deals: []};
        },
        componentDidMount: function() {
            this.loadDeals();
        },
        render: function() {
            return (
                    <h2>{this.state.deals.jcrew}</h2>
            );
        }
    });

ReactDOM.render(<CommentBox url="/deals" />, document.getElementById('jCrewContent'));