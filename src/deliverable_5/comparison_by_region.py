
'''Compares Airbnb and tenancy data by SA2 area and saves a static map locally.'''

import pandas
import numpy
import matplotlib.pyplot
import geopandas


def cleaning():
    pandas.set_option('display.max_columns', None)

    data = pandas.read_csv(
        'data/processed/christchurch_airbnb_tenancy_joined.csv',
        low_memory=False
    )

    data.columns = data.columns.str.strip()

    # Separate tenancy records from Airbnb records
    tenancy = data[data['Location Id'].notna()].copy()
    airbnb = data[data['Location Id'].isna()].copy()

    # Convert tenancy columns to numeric values
    tenancy['Location Id'] = pandas.to_numeric(
        tenancy['Location Id'], errors='coerce'
    )
    tenancy['Total Bonds'] = pandas.to_numeric(
        tenancy['Total Bonds'], errors='coerce'
    )

    # Remove rows with missing tenancy information
    tenancy = tenancy.dropna(
        subset=['Location Id', 'Total Bonds']
    ).copy()

    tenancy['Location Id'] = tenancy['Location Id'].astype(int)
    tenancy['Total Bonds'] = tenancy['Total Bonds'].astype(int)

    # Convert Airbnb SA2 codes to numeric values
    airbnb['sa22026_code'] = pandas.to_numeric(
        airbnb['sa22026_code'], errors='coerce'
    )

    print("Total Airbnb records:", len(airbnb))
    print(
        "Airbnb records with missing SA2 codes:",
        airbnb['sa22026_code'].isna().sum()
    )

    # Remove Airbnb records without SA2 codes
    airbnb = airbnb.dropna(subset=['sa22026_code']).copy()
    airbnb['sa22026_code'] = airbnb['sa22026_code'].astype(int)

    return tenancy, airbnb


def master():
    # Load the cleaned data
    tenancy, airbnb = cleaning()

    # Load the official SA2 shapefile
    sa2 = geopandas.read_file(
        'data/raw/statsnz-statistical-area-2-2026-SHP'
    )

    # Keep only the required columns
    sa2 = sa2[['SA22026_V1', 'SA22026__1', 'geometry']].copy()
    sa2['SA22026_V1'] = sa2['SA22026_V1'].astype(int)

    # Count Airbnb properties in each SA2 area
    airbnb_counts = airbnb['sa22026_code'].value_counts()
    sa2['AirBNB_Count'] = sa2['SA22026_V1'].map(airbnb_counts)

    # Combine tenancy records by SA2 code before merging
    tenancy_counts = (
        tenancy.groupby('Location Id', as_index=False)['Total Bonds']
        .sum()
    )

    # Merge tenancy counts with SA2 geographic areas
    sa2 = sa2.merge(
        tenancy_counts,
        left_on='SA22026_V1',
        right_on='Location Id',
        how='left'
    )

    # Rename columns for clarity
    sa2 = sa2.rename(columns={
        'SA22026_V1': 'SA2_2026_Code',
        'SA22026__1': 'SA2_2026_Name',
        'Total Bonds': 'Rental_Count'
    })

    # Replace missing counts with zero
    sa2['AirBNB_Count'] = pandas.to_numeric(
        sa2['AirBNB_Count'], errors='coerce'
    ).fillna(0)

    sa2['Rental_Count'] = pandas.to_numeric(
        sa2['Rental_Count'], errors='coerce'
    ).fillna(0)

    # Reset the index
    sa2 = sa2.reset_index(drop=True)

    # Create a static map showing Airbnb counts
    fig, ax = matplotlib.pyplot.subplots(figsize=(12, 8))

    sa2.plot(
        column='AirBNB_Count',
        legend=True,
        ax=ax,
        missing_kwds={
            'color': 'lightgrey',
            'label': 'No Airbnb records'
        }
    )

    ax.set_title('Airbnb Properties by SA2 Area')
    ax.set_axis_off()

    fig.tight_layout()

    # Save the map as a PNG image
    fig.savefig(
        'data/processed/sa2_areas_map.png',
        dpi=300,
        bbox_inches='tight'
    )

    matplotlib.pyplot.close(fig)

    print(
        'Static map saved to data/processed/sa2_areas_map.png'
    )


# Run the function when this script is executed directly
if __name__ == '__main__':
    master()