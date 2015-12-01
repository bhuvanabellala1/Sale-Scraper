/*
    Renders all the deals
 */
var DisplayDeals = React.createClass({
    render: function () {

        /* Uses map to go through each deal and render*/
          var display_deals = this.props.deals.map(function (deal, i) {
              return (
                  <Deal company = {deal.company} id = {i} image = {deal.image}
                      promo={deal.promo} details = {deal.details}/>
              );
          });

            return (
                <div>
                    {display_deals}
                </div>
            );
        }
      });

/*Componenet controls how each deal is presented */
var Deal =  React.createClass({

        getInitialState: function () {
          return {
              hover: false,
          };
        },

        mouseOver: function () {
          this.setState({hover: true});
        },

        mouseOut: function () {
          this.setState({hover: false});
        },

        displayDetails: function(){
           alert(this.props.details);
        },

        render: function() {
            var label = <img src={this.props.image} alt="J Crew Bag" width="150" height="120"/>;
             if (this.state.hover) { 
                label = this.props.promo;
                 console.log(label);
             } 
          return (
               <div id='dealDisplay' onMouseOver={this.mouseOver} onMouseOut={this.mouseOut} onClick={this.displayDetails}>{label}</div>
          );
        }
      });

/* Loads the deals */
var GetDeals = React.createClass({

        /* Make an ajax request to retrieve the deals */
        loadDeals: function() {
            console.log("here");
            $.ajax({
                url: this.props.url,
                dataType: 'json',
                cache: false,
                success: function(deals) {
                    this.setState({deals: deals});
                    console.log(deals);
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
                    <DisplayDeals deals={this.state.deals} />
                </div>
            );
        }
    });

ReactDOM.render(<GetDeals url="/deals" />, document.getElementById('jCrewContent'));