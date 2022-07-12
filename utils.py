"""Utility classes and functions for the link prediction project."""

from link_prediction.utils.classes import Design
from link_prediction.datasets.figma import FigmaDataPoint


class DataPoint(FigmaDataPoint):
    """Represents a potential link in a Figma design."""

    def __init__(
        self, design: Design, source: FigmaDataPoint.SourceData, target_id: str
    ) -> None:
        # Set unknown attributes to None
        self.application_id = None
        self.id = None
        self.is_link = None
        # Set known attributes
        self.source = source
        self.target_id = target_id
        # Compute pages and element from Design object
        self.source_page = design.find_page_by_id(source.page_id)
        self.source_element = self.source_page.find_by_id(source.id)
        self.target_page = design.find_page_by_id(target_id)


def get_data_points(design: Design) -> list[DataPoint]:
    """Returns a list of DataPoint objects representing
    all potential links from a Design object."""
    # Create a list of DataPoint objects
    data_points = []
    # Iterate over the pages in the design
    for page in design.pages:
        # Iterate over the elements in the page
        for element in page.elements:
            # Iterate over the other pages in the design
            for other_page in design.pages:
                if other_page.id == page.id:
                    continue
                # Create a DataPoint object for the element
                # linking to the other page
                data_point = DataPoint(
                    design=design,
                    source=FigmaDataPoint.SourceData(
                        id=element.id,
                        page_id=page.id,
                    ),
                    target_id=other_page.id,
                )
                # Add the DataPoint object to the list of DataPoint objects
                data_points.append(data_point)
    # Return the list of DataPoint objects
    return data_points
