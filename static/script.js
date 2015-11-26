
var HoverButton = React.createClass({
        getInitialState: function () {
          return {
            hover: false};
        },

        mouseOver: function () {
          this.setState({hover: true});
        },

        mouseOut: function () {
          this.setState({hover: false});
        },

        render: function() {
            var label = <img className="JcrewBag" src={'/static/jcrew.jpg'} alt="J Crew Bag"
                             width="150" height="120"/>;
             if (this.state.hover) { 
                label = this.props.deals.jcrew;
                 console.log(label);
             } 
            return React.createElement( 
                "box", 
                {  

                onMouseOver: this.mouseOver, onMouseOut: this.mouseOut},
                label  
            );

        }
      });

/* Loads the deals */
var GetDeals = React.createClass({

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
                <div className="loadDeals">
                    <h1> The Sale Shop</h1>
                    <table>
                        <tr>
                    <td className="dealsParagraph"><HoverButton deals={this.state.deals}/></td>
                            </tr>
                        </table>
                </div>
            );
        }
    });

ReactDOM.render(<GetDeals url="/deals" />, document.getElementById('jCrewContent'));