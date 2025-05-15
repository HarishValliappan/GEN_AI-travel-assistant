import { jsPDF } from 'jspdf';

export function generatePdf(recommendations) {
  const doc = new jsPDF();
  const companyName = 'WayfarerAI';
  const recommendationsTitle = 'Travel Recommendations';
  const margin = 10;
  let y = margin;

  // Function to add header and border to each page
  function addPageHeaderAndBorder(pageNumber) {
    // Reset y position for new page
    y = margin;

    // Add border to the page
    doc.rect(margin, margin, doc.internal.pageSize.getWidth() - 2 * margin, doc.internal.pageSize.getHeight() - 2 * margin);

    // Add company heading
    doc.setFontSize(10);
    doc.text(companyName + " - Page " + pageNumber, margin + 5, y + 5);
  }

  // // Add image background to the first page
  // const backgroundImage = 'frontend/src/assets/img1.avif'; // Path to your image
  // doc.addImage(backgroundImage, 'AVIF', margin, margin, doc.internal.pageSize.getWidth() - 2 * margin, doc.internal.pageSize.getHeight() - 2 * margin);

  // Add first page header and border
  addPageHeaderAndBorder(1);
  y += 20;

  // Add company heading
  doc.setFontSize(20);
  doc.text(companyName, margin, y);
  y += 15;

  // Add recommendations title
  doc.setFontSize(16);
  doc.text(recommendationsTitle, margin, y);
  y += 10;

  y += 5;

  // Add recommendations content
  doc.setFontSize(12);
  if (recommendations) {
    let pageNumber = 1;
    const textLines = doc.splitTextToSize(recommendations, doc.internal.pageSize.getWidth() - 2 * margin - 10);
    textLines.forEach((line, index) => {
      if (y > doc.internal.pageSize.getHeight() - margin - 10) {
        doc.addPage();
        pageNumber++;
        addPageHeaderAndBorder(pageNumber);
        y = margin + 10;
      }
      doc.text(line, margin + 10, y);
      y += 7;
    });
  } else {
    doc.text("No recommendations available.", margin + 10, y);
  }

  doc.save('recommendations.pdf');
}