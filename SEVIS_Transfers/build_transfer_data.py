from SEVIS_Transfers.build_new_student_data import file2, \
    wb2, old_sheet, new_sheet, row_max_old, col_max_old, final_sheet, \
    row_max_current, col_max_current, row_max_final, col_max_final


def copy_new_Range(startCol, startRow, endCol, endRow, old_sheet):
    """
    Copies a range of cells as a nested list
    Takes: start cell, end cell, and the sheet we want to copy from
    """
    rangeSelected = []
    for i in range(startRow, endRow+1, 1):
        rowSelected = []
        for j in range(startCol, endCol + 1, 1):
            rowSelected.append(old_sheet.cell(row = i, column = j).value)
        rangeSelected.append(rowSelected)

    return rangeSelected


def paste_new_Range(startCol, startRow, endCol, endRow, sheetReceiving, copiedData):
    countRow = 0
    for i in range(startRow, endRow+1, 1):
        countCol = 0
        for j in range(startCol, endCol+1, 1):
            sheetReceiving.cell(row=i, column=j).value = copiedData[countRow][countCol]
            countCol += 1
        countRow += 1


def create_new_Data():
    """Pastes copied range to new sheet which needs to be updates"""
    print(f'Old Row Range = {new_sheet.max_row}')
    print('Processing data...')

    if new_sheet.cell(row=1, column=1).value is None:
        selectedRange = copy_new_Range(1, 1, col_max_old, row_max_old, old_sheet)
        paste_new_Range(1, 1, col_max_old, row_max_old, new_sheet, selectedRange)

    elif new_sheet.cell(row=1, column=1).value == 'SEVIS ID':
        selectedRange = copy_new_Range(1, 2, col_max_old, row_max_old, old_sheet)
        paste_new_Range(1, (row_max_current+1), col_max_old, (row_max_current + row_max_old-1), new_sheet, selectedRange)

    wb2.save(file2)
    print("Range copied and pasted")
    print(f'New Row Range = {new_sheet.max_row}')


def paste_to_final():
    """Pastes copied range from new sheet to final sheet - do this after sorting data"""
    print(f'Current Row Range = {row_max_current}')
    print('Processing data...')
    selectedRange = copy_new_Range(1, 1, col_max_current, row_max_current, new_sheet)
    paste_new_Range(1, 1, col_max_current, row_max_current, final_sheet, selectedRange)
    wb2.save(file2)
    print("Range copied and pasted")
    print(f'New Row Range = {row_max_final}')


def grab_final_data():
    print(f'Current Row Range = {final_sheet.max_row}')
    print('Grabbing most recent data...')
    selectedRange = copy_new_Range(1, 1, col_max_final, row_max_final, final_sheet)
    paste_new_Range(1, 1, col_max_final, row_max_final, new_sheet, selectedRange)
    new_sheet.delete_rows(1)
    wb2.save(file2)
    print('Range copied and pasted')
    print(f'New Row Range = {new_sheet.max_row}')


paste_to_final()